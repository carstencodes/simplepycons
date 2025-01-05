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


class PapersWithCodeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "paperswithcode"

    @property
    def original_file_name(self) -> "str":
        return "paperswithcode.svg"

    @property
    def title(self) -> "str":
        return "Papers With Code"

    @property
    def primary_color(self) -> "str":
        return "#21CBCE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Papers With Code</title>
     <path d="M0 2v20h4.4v-2.4h-2V4.4h2V2H0Zm19.6
 0v2.4h2v15.2h-2V22H24V2h-4.4Zm-16 3.6v12.8H6V5.6H3.6Zm7.2
 0v12.8h2.4V5.6h-2.4Zm7.2
 0v12.8h2.4V5.6H18Zm-10.8.8v11.2h2.4V6.4H7.2Zm7.2
 0v11.2h2.4V6.4h-2.4Z" />
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
