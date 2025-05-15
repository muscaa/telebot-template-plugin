#include "ttp/plugin.h"

#include <telebot/events.h>
#include <imgui.h>

namespace ttp {

namespace log = telebot::utils::logging;

static void post_imgui_build() {
    ImGui::Begin("Template Plugin Window");

    ImGui::Text("This is some useful text.");

    if (ImGui::Button("Button")) {
        //counter++;
    }
    ImGui::End();
}

void main(const telebot::plugins::Plugin& plugin) {
    log::info("Hello from {}!", plugin.getName());

    telebot::events::post_imgui_build.connect(&post_imgui_build);
}

} // namespace ttp
