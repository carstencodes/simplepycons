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


class ZerotierIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "zerotier"

    @property
    def original_file_name(self) -> "str":
        return "zerotier.svg"

    @property
    def title(self) -> "str":
        return "ZeroTier"

    @property
    def primary_color(self) -> "str":
        return "#FFB441"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>ZeroTier</title>
     <path d="M4.01 0A3.999 3.999 0 0 0 .014 4v16c0 2.209 1.79 4 3.996
 4h15.98a3.998 3.998 0 0 0 3.996-4V4c0-2.209-1.79-4-3.996-4zm-.672
 2.834h17.326a.568.568 0 1 1 0
 1.137h-8.129c.021.059.033.123.033.19v1.804A6.06 6.06 0 0 1 18.057
 12c0 3.157-2.41 5.75-5.489 6.037v2.56a.568.568 0 1 1-1.136
 0v-2.56A6.061 6.061 0 0 1 5.943 12a6.06 6.06 0 0 1
 5.489-6.035V4.16c0-.066.012-.13.033-.19H3.338a.568.568 0 1 1
 0-1.136zm8.094 4.307A4.89 4.89 0 0 0 7.113 12a4.89 4.89 0 0 0 4.319
 4.86zm1.136 0v9.718A4.892 4.892 0 0 0 16.888 12a4.892 4.892 0 0
 0-4.32-4.86z" />
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
