#pragma once

#include <telebot/api.h>
#include <telebot/utils/logging.h>
#include <telebot/plugins.h>

namespace ttp {

EXPORT void main(const telebot::plugins::Plugin& plugin);

} // namespace ttp
