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


class AsusIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "asus"

    @property
    def original_file_name(self) -> "str":
        return "asus.svg"

    @property
    def title(self) -> "str":
        return "ASUS"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ASUS</title>
     <path d="M23.904 10.788V9.522h-4.656c-.972 0-1.41.6-1.482
 1.182v.018-1.2h-1.368v1.266h1.362zm-6.144.456l-1.368-.078v1.458c0
 .456-.228.594-1.02.594H14.28c-.654
 0-.93-.186-.93-.594v-1.596l-1.386-.102v1.812h-.03c-.078-.528-.276-1.14-1.596-1.23L6
 11.22c0 .666.474 1.062 1.218 1.14l3.024.306c.24.018.414.09.414.288 0
 .216-.18.24-.456.24H5.946V11.22l-1.386-.09v3.348h5.646c1.26 0
 1.662-.654 1.722-1.2h.03c.156.864.912 1.2 2.19 1.2h1.41c1.494 0
 2.202-.456 2.202-1.524zm4.398.258l-4.338-.258c0 .666.438 1.11 1.182
 1.17l3.09.24c.24.018.384.078.384.276 0
 .186-.168.258-.516.258h-4.212v1.29h4.302c1.356 0 1.95-.474 1.95-1.554
 0-.972-.534-1.338-1.842-1.422zm-10.194-1.98h1.386v1.266h-1.386zM3.798
 11.07l-1.506-.15L0 14.478h1.686zm7.914-1.548h-4.23c-.984
 0-1.416.612-1.518 1.2v-1.2H3.618c-.33
 0-.486.102-.642.33l-.648.936h9.384Z" />
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
