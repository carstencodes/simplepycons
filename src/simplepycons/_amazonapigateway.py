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


class AmazonApiGatewayIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "amazonapigateway"

    @property
    def original_file_name(self) -> "str":
        return "amazonapigateway.svg"

    @property
    def title(self) -> "str":
        return "Amazon API Gateway"

    @property
    def primary_color(self) -> "str":
        return "#FF4F8B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Amazon API Gateway</title>
     <path d="M9.456 18.7h1.258v-.865H9.456Zm2.115
 0h1.286v-.865h-1.286ZM6.43 1.127.857 3.892v17.19l5.572 1.885Zm.857
 5.47v11.238H8.57v.865H7.286v4.868a.434.434 0 0 1-.429.432.425.425 0 0
 1-.136-.022L.292 21.804a.432.432 0 0
 1-.292-.41V3.623c0-.164.093-.315.24-.388L6.668.045a.424.424 0 0 1
 .415.02.433.433 0 0 1 .203.367v5.3H8.57v.865ZM13.714
 18.7H15v-.865h-1.286Zm.028-12.103H15v-.864h-1.258Zm-2.143
 0h1.258v-.864H11.6Zm-2.143 0h1.258v-.864H9.456Zm13.687-2.705L17.57
 1.127v21.84l5.572-1.884ZM24 21.394c0 .186-.117.35-.292.41l-6.429
 2.174a.425.425 0 0 1-.386-.06.434.434 0 0
 1-.179-.35V18.7h-.829v-.865h.83V6.597h-.83v-.864h.83v-5.3c0-.15.076-.289.202-.368a.424.424
 0 0 1 .415-.02l6.428 3.19c.147.073.24.224.24.388ZM13.257
 9.346l-.8-.31-2.143 5.618.8.31Zm2.903 2.744a.434.434 0 0 0
 0-.612L14.446 9.75l-.606.612 1.411 1.423-1.411 1.423.606.611Zm-6.606
 1.728L7.84 12.09a.434.434 0 0 1 0-.612L9.554 9.75l.606.612-1.411
 1.423 1.411 1.423Z" />
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
            "AWS API Gateway",
        ]
