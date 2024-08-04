#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2024 Carsten Igel.
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


class AmazonEcTwoIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "amazonec2"

    @property
    def original_file_name(self) -> "str":
        return "amazonec2.svg"

    @property
    def title(self) -> "str":
        return "Amazon EC2"

    @property
    def primary_color(self) -> "str":
        return "#FF9900"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Amazon EC2</title>
     <path d="M6.429 17.571h10.714V6.857H6.429v10.714ZM18
 6.857h1.714v.857H18V9.43h1.714v.857H18v1.285h1.714v.858H18v1.714h1.714V15H18v1.714h1.714v.857H18v.059a.8.8
 0 0
 1-.799.799h-.058v1.714h-.857v-1.714H14.57v1.714h-.857v-1.714H12.43v1.714h-.858v-1.714H9.857v1.714H9v-1.714H7.286v1.714h-.857v-1.714H6.37a.8.8
 0 0
 1-.799-.8v-.058H4.286v-.857H5.57V15H4.286v-.857H5.57v-1.714H4.286v-.858H5.57v-1.285H4.286v-.857H5.57V7.714H4.286v-.857H5.57V6.8a.8.8
 0 0 1
 .8-.799h.058V4.286h.857V6H9V4.286h.857V6h1.714V4.286h.858V6h1.285V4.286h.857V6h1.715V4.286h.857V6h.058a.8.8
 0 0 1 .799.799v.058ZM12.429 23.09a.054.054 0 0
 1-.054.053H.91a.053.053 0 0
 1-.053-.053V11.625c0-.03.024-.054.053-.054h2.52v-.857H.91a.911.911 0
 0 0-.91.91V23.09c0 .502.408.91.91.91h11.465a.91.91 0 0 0
 .91-.91V21h-.856ZM24 .91v11.465a.91.91 0 0
 1-.91.91h-2.52v-.856h2.519a.054.054 0 0 0 .053-.054V.91a.053.053 0 0
 0-.053-.053H11.625a.053.053 0 0
 0-.054.053v2.52h-.857V.91c0-.502.409-.91.91-.91H23.09a.91.91 0 0 1
 .91.91Z" />
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
        yield from [
            "Amazon Elastic Compute Cloud",
            "AWS EC2",
            "AWS Elastic Compute Cloud",
        ]