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


class KickstarterIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "kickstarter"

    @property
    def original_file_name(self) -> "str":
        return "kickstarter.svg"

    @property
    def title(self) -> "str":
        return "Kickstarter"

    @property
    def primary_color(self) -> "str":
        return "#05CE78"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Kickstarter</title>
     <path d="M7.168 0c-3.2 0-5.797 2.579-5.797 5.758v12.484C1.371
 21.42 3.968 24 7.168 24c1.981 0 3.716-.978 4.768-2.479l.794.79c2.26
 2.245 5.943 2.245 8.203 0a5.724 5.724 0 001.696-4.075 5.724 5.724 0
 00-1.696-4.074l-2.182-2.168 2.182-2.156a5.724 5.724 0 001.696-4.074
 5.724 5.724 0 00-1.696-4.074c-2.26-2.246-5.942-2.246-8.203
 0l-.794.789A5.797 5.797 0 007.168 0Z" />
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
