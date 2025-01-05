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


class ExoscaleIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "exoscale"

    @property
    def original_file_name(self) -> "str":
        return "exoscale.svg"

    @property
    def title(self) -> "str":
        return "Exoscale"

    @property
    def primary_color(self) -> "str":
        return "#DA291C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Exoscale</title>
     <path d="M12 1.608 0 22.392h1.665L12 4.593v2.929l-8.612
 14.87H5.11L12 10.507v2.986l-5.167 8.9h1.722L12 16.477v2.929l-1.722
 2.985H24Z" />
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
