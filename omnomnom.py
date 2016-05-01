# Copyright (C) 2016  Max Rosin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import canteens.matheparser
import canteens.sing
import canteens.studentenwerk
import telegram
import time

class OmNomNom:
  def menu_makantine(bot, update):
    text = canteens.matheparser.get_menu(time.strftime('%d.%m.%Y'))
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

  def menu_marchstrasse(bot, update):
    text = canteens.studentenwerk.menu_mar()
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

  def menu_architektur(bot, update):
    text = canteens.studentenwerk.menu_a()
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

  def menu_acker(bot, update):
    text = canteens.studentenwerk.menu_acker()
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

  def menu_mensa(bot, update):
    text = canteens.studentenwerk.menu_mensa()
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

  def menu_tel(bot, update):
    text = canteens.studentenwerk.menu_tel()
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

  def menu_tu_sing(bot, update):
    text = canteens.sing.get_menu()
    bot.sendMessage(chat_id=update.message.chat_id, text=text, parse_mode=telegram.ParseMode.MARKDOWN)

# HU Berlin

  def menu_hu_nord(bot, update):
    text = canteens.studentenwerk.menu_hu_nord()
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

  def menu_hu_sued(bot, update):
    text = canteens.studentenwerk.menu_hu_sued()
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

  def menu_hu_adlershof(bot, update):
    text = canteens.studentenwerk.menu_hu_adlershof()
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

  def menu_hu_spandauer(bot, update):
    text = canteens.studentenwerk.menu_hu_spandauer()
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

# FU Berlin

  def menu_fu_1(bot, update):
    text = canteens.studentenwerk.menu_fu_1()
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

  def menu_fu_2(bot, update):
    text = canteens.studentenwerk.menu_fu_2()
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

  def menu_fu_lankwitz(bot, update):
    text = canteens.studentenwerk.menu_fu_lankwitz()
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

  def menu_fu_assmannshauser(bot, update):
    text = canteens.studentenwerk.menu_fu_assmannshauser()
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

  def menu_fu_dueppel(bot, update):
    text = canteens.studentenwerk.menu_fu_dueppel()
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

  def menu_fu_cafeteria(bot, update):
    text = canteens.studentenwerk.menu_fu_cafeteria()
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

  def menu_fu_cafe_koenigin_luise(bot, update):
    text = canteens.studentenwerk.menu_fu_cafe_koenigin_luise()
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

  def menu_fu_cafe_vant_hoff(bot, update):
    text = canteens.studentenwerk.menu_fu_cafe_vant_hoff()
    bot.sendMessage(chat_id=update.message.chat_id, text=text)

  def menu_fu_cafe_ihne(bot, update):
    text = canteens.studentenwerk.menu_fu_cafe_ihne()
    bot.sendMessage(chat_id=update.message.chat_id, text=text)
