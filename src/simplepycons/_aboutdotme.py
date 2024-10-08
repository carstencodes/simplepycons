#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class AboutdotmeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "aboutdotme"

    @property
    def original_file_name(self) -> "str":
        return "aboutdotme.svg"

    @property
    def title(self) -> "str":
        return "About.me"

    @property
    def primary_color(self) -> "str":
        return "#333333"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>About.me</title>
     <path d="M11.427 16.615v-6.042c0-.997-.444-1.669-1.541-1.669-.906
 0-1.754.614-2.159
 1.228v6.483H5.704v-6.042c0-.997-.423-1.669-1.523-1.669-.905
 0-1.734.633-2.158 1.228v6.483H0V7.351h2.023v1.247C2.428 8.04 3.642
 7.12 5.068 7.12c1.386 0 2.235.69 2.543 1.688.52-.825 1.754-1.688
 3.16-1.688 1.697 0 2.68.92 2.68 2.8v6.694h-2.024zM24
 12.163c0-2.925-1.788-5.042-4.604-5.042-2.777 0-4.759 2.174-4.759
 4.869 0 2.945 2.079 4.888 4.913 4.89 1.476 0 2.855-.482
 3.807-1.368l-.932-1.328c-.68.673-1.747 1.04-2.68 1.04-1.768
 0-2.815-1.174-2.971-2.56H24v-.5zm-7.245-.943c.077-1.116.893-2.444
 2.622-2.444 1.845 0 2.602 1.347 2.66 2.444h-5.282z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return ''''''

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
