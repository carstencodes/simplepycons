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


class SennheiserIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "sennheiser"

    @property
    def original_file_name(self) -> "str":
        return "sennheiser.svg"

    @property
    def title(self) -> "str":
        return "Sennheiser"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Sennheiser</title>
     <path d="M0 3v18h24V3zm13.209 1.659c-1.428.548-2.799 1.757-3.905
 4.182-.321.703-.925 2.062-1.2 2.67-2.224 4.882-3.364 5.932-6.72
 5.932V4.35H13.15c.184-.011.235.25.06.309zm9.428
 1.894V19.65H10.851c-.181.005-.227-.25-.055-.309 1.427-.548
 2.798-1.757 3.904-4.182.321-.703.926-2.062 1.2-2.67 2.22-4.882
 3.36-5.932 6.716-5.932z" />
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
