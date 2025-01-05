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


class RemedyEntertainmentIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "remedyentertainment"

    @property
    def original_file_name(self) -> "str":
        return "remedyentertainment.svg"

    @property
    def title(self) -> "str":
        return "Remedy Entertainment"

    @property
    def primary_color(self) -> "str":
        return "#D6001C"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Remedy Entertainment</title>
     <path d="M13.717 5.245v6.613a3.309 3.309 0 0 0 3.306-3.307 3.31
 3.31 0 0 0-3.306-3.306Zm-4.594 0h-3.45v6.613h3.455a3.309 3.309 0 0 0
 3.306-3.307 3.312 3.312 0 0 0-3.311-3.306Zm11.448 9.915v-1.507a8.578
 8.578 0 0 1-2.714 2.379l2.714 4.792v-2.878L24
 24h-7.574l-2.709-4.789V24h-1.656l-3.907-6.897H5.673V24H0V0h9.123a8.5
 8.5 0 0 1 4.589 1.337V0a8.551 8.551 0 0 1 6.859 3.441V1.939a8.527
 8.527 0 0 1 3.133 6.612 8.516 8.516 0 0 1-3.133 6.609Z" />
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
