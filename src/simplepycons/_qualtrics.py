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


class QualtricsIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "qualtrics"

    @property
    def original_file_name(self) -> "str":
        return "qualtrics.svg"

    @property
    def title(self) -> "str":
        return "Qualtrics"

    @property
    def primary_color(self) -> "str":
        return "#00B4EF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Qualtrics</title>
     <path d="M20.14 5.518l-2.695 9.538h-.034l-2.89-9.538H8.125l-2.19
 3.893-2.318-3.893H.368l3.78 6.116L0 18.486h2.993l2.66-4.534 2.755
 4.534h4.906v-8.99h.034q.102.564.195.966.093.402.175.744c.057.228.118.445.184.65.065.206.132.43.2.677l1.926
 5.949h2.523l1.942-5.95q.213-.718.398-1.385a14.544 14.544 0 0 0
 .32-1.506h.035v8.845H24V5.514zM7.373 11.651l3.383-5.616v11.118z" />
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
