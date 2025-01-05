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


class AutomatticIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "automattic"

    @property
    def original_file_name(self) -> "str":
        return "automattic.svg"

    @property
    def title(self) -> "str":
        return "Automattic"

    @property
    def primary_color(self) -> "str":
        return "#3499CD"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Automattic</title>
     <path d="M14.521 8.11a1.497 1.497 0 01.433 2.102l-3.511
 5.441a1.496 1.496 0 01-2.068.457 1.507 1.507 0
 01-.44-2.08l3.513-5.44c.215-.335.554-.57.943-.655.39-.085.796-.04
 1.13.175z M11.98 23.03C4.713 23.03 0 17.79 0 12.338v-.676C0 6.117
 4.713.97 11.98.97 19.246.97 24 6.117 24 11.662v.676c0 5.453-4.713
 10.692-12.02 10.692zm8.133-11.31c0-3.974-2.888-7.51-8.133-7.51-5.245
 0-8.087 3.542-8.087 7.51v.497c0 3.974 2.888 7.578 8.087 7.578 5.198 0
 8.133-3.604 8.133-7.578v-.497z" />
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
