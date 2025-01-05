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


class AutocadIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "autocad"

    @property
    def original_file_name(self) -> "str":
        return "autocad.svg"

    @property
    def title(self) -> "str":
        return "AutoCAD"

    @property
    def primary_color(self) -> "str":
        return "#E51050"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>AutoCAD</title>
     <path d="M3.8672 1.0527v.0157L0
 3.3848v17.914l3.8965-2.332h18.3398V2.3301c0-.702-.5773-1.2774-1.2793-1.2774H3.8672zm7.5058
 4.0098h3.3008l2.9844 9.9512h-2.5879l-.5683-2.1895h-2.9844l-.5703
 2.1621h-2.416l2.8417-9.9238zm11.8633.0273v14.877H4.172l-2.0684
 1.2383v.4648c0 .702.5793 1.2774 1.2813
 1.2774H24V5.0898h-.7637zM12.9668 6.6816l-.9941
 4.3243h2.0468l-1.0527-4.3243z" />
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
