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


class FilesIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "files"

    @property
    def original_file_name(self) -> "str":
        return "files.svg"

    @property
    def title(self) -> "str":
        return "Files"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Files</title>
     <path d="M12.367 2.453a.822.822 0 0 0-.576.238L.241
 14.213a.822.822 0 0
 0-.241.584v.066c0-.323.209-.608.516-.709l7.275-2.318a2.437 2.437 0 0
 0 1.584-1.592l2.318-7.267a.757.757 0 0 1 .719-.524zM0 14.863v5.047c0
 .904.733 1.637 1.637 1.637h20.726c.904 0 1.637-.733
 1.637-1.637V4.09c0-.904-.733-1.637-1.637-1.637h-9.951v.5l.088
 9.861c.01 1.175-.962 2.14-2.137 2.14L0 14.862zM12 3.66l-2.148
 6.735v.001a2.94 2.94 0 0 1-1.909 1.916l-6.716 2.141h9.136c.905 0
 1.638-.734 1.637-1.639zm-10.363.975c-.905 0-1.638.734-1.637
 1.638v7.473l9.135-9.111Z" />
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
