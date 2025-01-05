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


class KashflowIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kashflow"

    @property
    def original_file_name(self) -> "str":
        return "kashflow.svg"

    @property
    def title(self) -> "str":
        return "KashFlow"

    @property
    def primary_color(self) -> "str":
        return "#E5426E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>KashFlow</title>
     <path d="M16.278 2.141l-.83 2.702C8.007.174 2.958 4.724 2.958
 4.724-1.638 8.564.49 14.678.495 14.678 1.252-.016 14.24 8.943 14.24
 8.943c-.237 1.066-.996 2.63-.972 2.654l8.508-1.256zm7.228
 7.181C22.747 24.016 9.76 15.057 9.76 15.057c.332-1.066 1.02-2.654
 1.02-2.607L2.27 13.66l5.451 8.2.83-2.702c7.441 4.669 12.49.119
 12.49.119 4.597-3.84 2.464-9.954 2.464-9.954z" />
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
