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


class ConstructThreeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "construct3"

    @property
    def original_file_name(self) -> "str":
        return "construct3.svg"

    @property
    def title(self) -> "str":
        return "Construct 3"

    @property
    def primary_color(self) -> "str":
        return "#00FFDA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Construct 3</title>
     <path d="M12.392 0c-6.752 0-12 5.498-12 12 0 6.574 5.313 12 12 12
 4.283 0 8.087-2.254 10.217-5.704a.571.571 0 0
 0-.2-.795l-5.55-3.204a.572.572 0 0 0-.76.177 4.453 4.453 0 0 1-3.707
 1.983c-2.458 0-4.458-2-4.458-4.457 0-2.458 2-4.457 4.458-4.457 1.491
 0 2.877.741 3.707 1.983a.571.571 0 0 0 .76.177l5.55-3.204a.571.571 0
 0 0 .2-.795A11.998 11.998 0 0 0 12.392 0zm0 3.527c3.048 0 5.72 1.61
 7.213 4.026l-2.99 1.726c-.037.021-.085.013-.108-.026a4.942 4.942 0 0
 0-4.115-2.2A4.953 4.953 0 0 0 7.445 12c0 .9.241 1.745.663
 2.473l-2.342 1.353a.327.327 0 0 0-.112.458 7.977 7.977 0 0 0 6.738
 3.7 7.978 7.978 0 0 0 6.789-3.781l2.983 1.722a.08.08 0 0 1 .028.113
 11.447 11.447 0 0 1-9.8 5.472C6.045 23.51.882 18.346.882
 12c0-2.095.562-4.06 1.544-5.754l2.35
 1.356c.15.088.345.04.439-.11a8.467 8.467 0 0 1 7.177-3.966zM22.965
 8.95a.666.666 0 0 0-.336.088l-4.149 2.395a.654.654 0 0 0 0
 1.131l4.149 2.396c.434.25.98-.064.98-.566v-4.79a.655.655 0 0
 0-.644-.654zm-.663 1.785v2.528L20.112 12z" />
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
