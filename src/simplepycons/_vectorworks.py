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


class VectorworksIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "vectorworks"

    @property
    def original_file_name(self) -> "str":
        return "vectorworks.svg"

    @property
    def title(self) -> "str":
        return "Vectorworks"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Vectorworks</title>
     <path d="M12 0C5.4 0 0 5.4 0 12s5.4 12 12 12 12-5.4 12-12S18.6 0
 12 0zm0 22.725c-5.925 0-10.725-4.8-10.725-10.725S6.075 1.275 12 1.275
 22.725 6.075 22.725 12 17.925 22.725 12 22.725zM8.775 7.5h-2.25c-.15
 0-.208.086-.15.225l4.425 10.65c.04.098.15.225.3.225h1.95c.15 0
 .206-.086.15-.225l-4.35-10.8c-.028-.07-.035-.075-.075-.075zm8.7
 0h-2.25c-.075 0-.13.023-.15.075L13.35 11.85a.6.6 0 0 0 0 .375l1.05
 2.55c.075.15.225.15.3 0l2.925-7.05c.057-.139 0-.225-.15-.225z" />
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
