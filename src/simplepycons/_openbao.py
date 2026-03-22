#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class OpenbaoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "openbao"

    @property
    def original_file_name(self) -> "str":
        return "openbao.svg"

    @property
    def title(self) -> "str":
        return "OpenBao"

    @property
    def primary_color(self) -> "str":
        return "#336D5C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OpenBao</title>
     <path d="M11.997 4.631a3 3 0 0 0-.309.02c-3.277.098-6.427
 1.737-8.084 4.74a8.2 8.2 0 0 0-.99 3.117C.922 13.256 0 14.185 0
 15.142c0 1.12 1.264 2.196 3.515 2.989 2.25.793 5.302 1.238 8.485
 1.238s6.235-.445 8.485-1.238S24 16.263 24
 15.14c0-.956-.922-1.885-2.614-2.633a8.2 8.2 0 0
 0-.99-3.117c-1.657-3.003-4.807-4.642-8.084-4.74a3 3 0 0 0-.315-.02m.9
 2.09.037.02c.354.198.687.488.737.547.317.38.74 1.09.74 1.473a.896.896
 0 0 0 1.793 0 3.24 3.24 0 0 0-.322-1.39 7.2 7.2 0 0 1 2.945
 2.886c.676 1.226.902 2.634.75 3.605-.077.486-.244.847-.419
 1.046s-.32.278-.622.278H5.464c-.301
 0-.447-.079-.622-.278-.175-.2-.342-.56-.419-1.046-.152-.97.074-2.38.75-3.605A7.2
 7.2 0 0 1 8.118 7.37a3.24 3.24 0 0 0-.322 1.39.896.896 0 0 0 1.792
 0c0-.382.424-1.093.741-1.473a3.7 3.7 0 0 1 .775-.567v2.04a.896.896 0
 1 0 1.792 0zm2.141 3.523a1.38 1.38 0 0
 0-1.138.61c-.21.309-.278.562.151.827.28.173.605.11.795.016.124-.06.17-.107.387-.007.439.203.695.193.948-.017.284-.236.236-.58.023-.83-.306-.359-.72-.591-1.166-.599m-6.797.017c-.445.007-.86.24-1.167.6-.213.25-.26.593.024.829.253.21.51.22.948.017.217-.1.263-.053.386.007.191.093.516.156.796-.016.429-.265.36-.519.15-.827a1.38
 1.38 0 0 0-1.137-.61" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/openbao/artwork/blob/8f759'''

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
