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


class HiBobIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "hibob"

    @property
    def original_file_name(self) -> "str":
        return "hibob.svg"

    @property
    def title(self) -> "str":
        return "Hi Bob"

    @property
    def primary_color(self) -> "str":
        return "#E42C51"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Hi Bob</title>
     <path d="M12.527 17.538c-2.077 0-3.767-1.705-3.767-3.8 0-2.096
 1.69-3.8 3.767-3.8s3.767 1.704 3.767 3.8c0 2.095-1.69 3.8-3.766
 3.8m0-6.408c-1.426 0-2.586 1.17-2.586 2.607 0 1.439 1.159 2.609 2.585
 2.609s2.585-1.17 2.585-2.609c0-1.437-1.16-2.606-2.585-2.606M1.707
 10.4V7.082a.858.858 0 0 0-.853-.86.856.856 0 0 0-.854.86v6.632c.002
 2.244 1.81 4.065 4.03 4.065 2.221 0 4.029-1.823 4.029-4.065
 0-2.24-1.808-4.063-4.029-4.063a3.98 3.98 0 0 0-2.323.748zm2.323
 5.658a2.335 2.335 0 0 1-2.323-2.343 2.335 2.335 0 0 1 2.323-2.342
 2.335 2.335 0 0 1 2.323 2.342 2.335 2.335 0 0 1-2.323
 2.343m16.465-5.854a3.49 3.491 0 0 0-2.848 1.484V6.704a.33.33 0 0
 0-.327-.331.33.33 0 0 0-.328.331v7.036c.002 1.949 1.572 3.533 3.504
 3.533 1.931 0 3.504-1.586 3.504-3.536
 0-1.949-1.573-3.534-3.505-3.534m0 6.408c-1.57
 0-2.847-1.289-2.847-2.873s1.278-2.872 2.847-2.872c1.57 0 2.848 1.288
 2.848 2.872 0 1.585-1.277 2.873-2.848 2.873" />
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
        yield from [
            "Bob",
        ]
