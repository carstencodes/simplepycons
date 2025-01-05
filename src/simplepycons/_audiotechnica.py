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


class AudiotechnicaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "audiotechnica"

    @property
    def original_file_name(self) -> "str":
        return "audiotechnica.svg"

    @property
    def title(self) -> "str":
        return "Audio-Technica"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Audio-Technica</title>
     <path d="M12 0A11.992 11.992 0 00.015 11.985 12.019 12.019 0 0012
 24a12.019 12.019 0 0011.985-12.015A11.992 11.992 0 0012.004 0zm0
 .903a11.078 11.078 0 0111.085 11.078c0 6.123-4.958 11.112-11.085
 11.112A11.104 11.104 0 01.922 11.985 11.078 11.078 0
 0111.996.907zm.087 1.16l-.43 1.252-5.674
 16.063-.204.604h12.654l-.23-.604L12.524 3.31zm0 2.797l2.007
 5.643-3.024 8.553H7.056zm2.502 7.038l2.532 7.155h-5.09z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://commons.wikimedia.org/wiki/File:Audio'''

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
