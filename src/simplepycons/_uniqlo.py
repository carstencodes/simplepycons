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


class UniqloIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "uniqlo"

    @property
    def original_file_name(self) -> "str":
        return "uniqlo.svg"

    @property
    def title(self) -> "str":
        return "Uniqlo"

    @property
    def primary_color(self) -> "str":
        return "#FF0000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Uniqlo</title>
     <path d="M0 0v24h24V0H0zm3.006 3.236h1.52v5.051a1.007 1.007 0 1 0
 2.014 0v-5.05h1.517v5.056a2.525 2.525 0 1 1-5.051 0V3.236zm7.07
 0h1.514l2.023 4.328V3.236h1.516v7.575h-1.516L11.59
 6.482v4.329h-1.514V3.236zm7.569.01h1.488v7.576h-1.488V3.246zM5.533
 13.078a2.526 2.526 0 0 1 2.524 2.53v2.523a2.51 2.51 0 0 1-.75
 1.793l.75 2.248H6.539l-.518-1.563a2.472 2.472 0 0 1-.488.043 2.524
 2.524 0 0 1-2.527-2.521v-2.524a2.527 2.527 0 0 1 2.527-2.529zm4.547
 0h1.514v6.057h3.535v1.517H10.08v-7.574zm8.336 0a2.526 2.526 0 0 1
 2.523 2.53v2.523a2.525 2.525 0 0 1-2.523 2.521 2.53 2.53 0 0
 1-2.531-2.521v-2.524a2.533 2.533 0 0 1 2.531-2.529zm-12.88 1.52a1.007
 1.007 0 0 0-1.01 1.01v2.523c0 .552.45 1.006 1.01 1.006.558 0
 1.003-.454 1.003-1.006v-2.524c0-.559-.445-1.01-1.004-1.01zm12.88
 0a1.01 1.01 0 0 0-1.012 1.01v2.523c0 .552.453 1.006 1.012 1.006a1.012
 1.012 0 0 0 1.01-1.006v-2.524c0-.559-.455-1.01-1.01-1.01z" />
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
