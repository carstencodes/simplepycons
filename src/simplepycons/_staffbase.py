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


class StaffbaseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "staffbase"

    @property
    def original_file_name(self) -> "str":
        return "staffbase.svg"

    @property
    def title(self) -> "str":
        return "Staffbase"

    @property
    def primary_color(self) -> "str":
        return "#00A4FD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Staffbase</title>
     <path d="M11.847 20.095a7.805 7.805 0
 01-6.286-3.238l1.714-1.238C8.323 17.048 10.037 18 11.847
 18s3.523-.857 4.571-2.381l1.714 1.238a7.805 7.805 0 01-6.285
 3.238zm.19-18c1.62 0 3.238.476 4.762 1.334l1.048.476 2.857-.572-.477
 2.857c2.381 3.715 2.191 9.239-1.047 12.667a9.748 9.748 0 01-7.048
 3.048 9.98 9.98 0 01-6.857-2.762c-3.905-3.81-4-10-.286-13.905
 1.905-2.095 4.477-3.143 7.048-3.143m0-2.095C8.799 0 5.751 1.333 3.466
 3.714c-4.572 4.762-4.477 12.381.285 16.953A11.91 11.91 0 0012.037
 24c3.238 0 6.381-1.333 8.571-3.619 3.62-3.714 4.286-9.81
 1.81-14.571l.38-2.096.477-2.952-2.952.571-2.19.381-.382-.19C15.941.476
 14.037 0 12.037 0Z" />
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
