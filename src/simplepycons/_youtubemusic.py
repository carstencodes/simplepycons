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


class YoutubeMusicIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "youtubemusic"

    @property
    def original_file_name(self) -> "str":
        return "youtubemusic.svg"

    @property
    def title(self) -> "str":
        return "YouTube Music"

    @property
    def primary_color(self) -> "str":
        return "#FF0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>YouTube Music</title>
     <path d="M12 0C5.376 0 0 5.376 0 12s5.376 12 12 12 12-5.376
 12-12S18.624 0 12 0zm0 19.104c-3.924 0-7.104-3.18-7.104-7.104S8.076
 4.896 12 4.896s7.104 3.18 7.104 7.104-3.18 7.104-7.104
 7.104zm0-13.332c-3.432 0-6.228 2.796-6.228 6.228S8.568 18.228 12
 18.228s6.228-2.796 6.228-6.228S15.432 5.772 12 5.772zM9.684
 15.54V8.46L15.816 12l-6.132 3.54z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://partnermarketinghub.withgoogle.com/#/'''

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
