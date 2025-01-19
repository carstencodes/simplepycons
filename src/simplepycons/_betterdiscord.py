#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2025 Carsten Igel.
#
# This file is part of simplepycons
# (see https://github.com/carstencodes/simplepycons).
#
# This file is published using the MIT license.
# Refer to LICENSE for more information
#
""""""
# pylint: disable=C0302
# Justification: Code is generated

from typing import TYPE_CHECKING

from .base_icon import Icon

if TYPE_CHECKING:
    from collections.abc import Iterable


class BetterdiscordIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "betterdiscord"

    @property
    def original_file_name(self) -> "str":
        return "betterdiscord.svg"

    @property
    def title(self) -> "str":
        return "BetterDiscord"

    @property
    def primary_color(self) -> "str":
        return "#3E82E5"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>BetterDiscord</title>
     <path d="M14.393.861q.514.258.964.57a6.6 6.6 0 0 1 2.122
 2.387c.513.987.792 2.133.828 3.409v9.556c-.035 1.275-.313 2.422-.828
 3.408a6.6 6.6 0 0 1-2.122 2.387 8 8 0 0 1-.933.555h.933c4.46.024
 8.643-2.205 8.643-7.315V8.352c.024-5.21-4.16-7.49-8.62-7.49zM0
 .867v9.197l5.693 5.127V5.44h3.31c3.537 0 3.537 4.444 0
 4.444H6.817v4.244h2.188c3.536 0 3.536 4.441 0 4.441H0v4.57h8.904c4.59
 0 8.151-1.836 8.278-6.388 0-2.094-.574-3.66-1.584-4.748 1.01-1.087
 1.584-2.652 1.584-4.746-.125-4.553-3.687-6.39-8.278-6.39z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/BetterDiscord/docs/blob/a6'''

    @property
    def license(self) -> "tuple[str | None, str | None]":
        _type: "str | None" = ''''''
        _url: "str | None" = ''''''

        if _type is not None and len(_type) == 0:
            _type = None

        if _url is not None and len(_url) == 0:
            _url = None

        return _type, _url

    @property
    def aliases(self) -> "Iterable[str]":
        yield from []
