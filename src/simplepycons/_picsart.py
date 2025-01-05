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


class PicsartIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "picsart"

    @property
    def original_file_name(self) -> "str":
        return "picsart.svg"

    @property
    def title(self) -> "str":
        return "Picsart"

    @property
    def primary_color(self) -> "str":
        return "#C209C1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Picsart</title>
     <path d="M11.999 0h-.012c-2.21 0-4.3.863-5.888
 2.432-.15.148-.428.458-.428.458-.096.11-.188.22-.276.334l-.036.047a8.683
 8.683 0 0 0-1.836 5.016v15.41a.32.32 0 0 0 .05.17.304.304 0 0 0
 .254.133h2.881a.303.303 0 0 0
 .305-.304v-7.843c0-.054.037-.08.053-.087a.1.1 0 0 1 .104.008 8.293
 8.293 0 0 0 4.815 1.525c1.32 0 2.547-.305 3.68-.86 2.847-1.392
 4.812-4.356 4.812-7.793 0-4.78-3.796-8.645-8.478-8.645zm-.013
 13.994c-2.841 0-5.152-2.396-5.152-5.34 0-2.946 2.31-5.342 5.152-5.342
 2.841 0 5.152 2.396 5.152 5.341 0 2.945-2.31 5.341-5.152 5.341z" />
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
