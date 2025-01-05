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


class TwoKIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "2k"

    @property
    def original_file_name(self) -> "str":
        return "2k.svg"

    @property
    def title(self) -> "str":
        return "2K"

    @property
    def primary_color(self) -> "str":
        return "#DD0700"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>2K</title>
     <path d="M0 .002v23.997h24V.002H0Zm10.962 5.592c2.36 0 4.443.416
 3.799 2.423-.434 1.365-2.017 1.918-3.114
 2.109l-2.757.489c-.655.114-1.039.277-1.3.549h6.012l-.818 2.529
 3.446-2.529h3.755l-4.091 2.772 2.07
 4.402h-3.766l-1.082-2.754-1.197.826-.619
 1.928H8.471l1.718-5.374h-6.25C4.874 10.2 6.891 9.36 8.731
 8.989l2.264-.457c.387-.07.64-.259.736-.557.136-.416-.32-.581-.994-.581-.784
 0-1.604.074-1.984 1.005H5.646c1.009-2.474 3.483-2.805 5.316-2.805Z"
 />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://support.2k.com/hc/en-us/articles/2039'''

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
