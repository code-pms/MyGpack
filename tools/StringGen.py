# Copyright (C) 2021 MyGpack

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from os import environ, path
from asyncio import get_event_loop
from pyrogram import Client
from dotenv import load_dotenv


if path.isfile("config.env"):
    load_dotenv("config.env")


async def genStrSession() -> None:
    async with Client(
        "X",
        api_id=int(environ.get("API_ID") or input("Enter Telegram APP ID: ")),
        api_hash=environ.get("API_HASH") or input("Enter Telegram API HASH: "),
    ) as app:
        print("\nprocessing...")
        await app.send_message(
            "me", f"#X #HU_STRING_SESSION\n\n```{await app.export_session_string()}```"
        )
        print("Done !, session string has been sent to saved messages!")


if __name__ == "__main__":
    get_event_loop().run_until_complete(genStrSession())
