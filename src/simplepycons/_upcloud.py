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


class UpcloudIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "upcloud"

    @property
    def original_file_name(self) -> "str":
        return "upcloud.svg"

    @property
    def title(self) -> "str":
        return "UpCloud"

    @property
    def primary_color(self) -> "str":
        return "#7B00FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>UpCloud</title>
     <path d="M22.1155 12.9964a1.8845 1.8845 0 110
 3.769H8.6643V11.87h.888v4.0072h12.5849a1.0078 1.0078 0 00.9964-.9964
 1.0317 1.0317 0
 00-1.0397-.9964H10.397v-.888zm-8.6859-5.7617H8.6643v1.9927h.888V8.1011h3.899a1.0078
 1.0078 0 01.9964.9964 1.0653 1.0653 0 01-1.018 1.0397H1.8845a1.8845
 1.8845 0 100 3.769h5.8917v-.8881H1.8845a.9964.9964 0
 010-1.9928h11.5668a1.8999 1.8999 0 001.8844-1.8845 1.9375 1.9375 0
 00-1.9061-1.9061z" />
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
