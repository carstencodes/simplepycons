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


class ContributorCovenantIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "contributorcovenant"

    @property
    def original_file_name(self) -> "str":
        return "contributorcovenant.svg"

    @property
    def title(self) -> "str":
        return "Contributor Covenant"

    @property
    def primary_color(self) -> "str":
        return "#5E0D73"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Contributor Covenant</title>
     <path d="M12.688 0c-6.627 0-12 5.373-12 12s5.373 12 12 12a12 12 0
 0 0 10.624-6.412 10.484 10.484 0 0 1-8.374 4.162c-5.799
 0-10.5-4.701-10.5-10.5S9.14.75 14.938.75c1.001 0 1.97.14
 2.887.402A11.956 11.956 0 0 0 12.688 0Zm2.438 2.25a9 9 0 1 0 7.967
 13.19 7.875 7.875 0 1 1-4.115-12.326 8.962 8.962 0 0 0-3.852-.864Z"
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
