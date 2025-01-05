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


class ImagedotscIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "imagedotsc"

    @property
    def original_file_name(self) -> "str":
        return "imagedotsc.svg"

    @property
    def title(self) -> "str":
        return "Image.sc"

    @property
    def primary_color(self) -> "str":
        return "#039CB2"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Image.sc</title>
     <path d="M13.6584 15.8117h.2543a.437.437 0 0 1
 .4369.4369v3.7998a.437.437 0 0 1-.4369.4369h-3.7998a.437.437 0 0
 1-.437-.4369v-.1225L6.839 21.5736v.6354c0 .6148.4984 1.1132 1.1132
 1.1132h8.121c.6148 0 1.1132-.4984
 1.1132-1.1132v-8.121c0-.6148-.4984-1.1132-1.1132-1.1132h-4.0561zm-.807-3.3369
 2.0123-3.5311c.3044-.5341.9843-.7204 1.5184-.416l7.0557
 4.021c.5341.3044.7204.9843.416 1.5184l-4.021
 7.0557c-.3044.5342-.9843.7205-1.5184.416l-.6279-.3578v-3.2653l.1554.0886a.437.437
 0 0 0 .5959-.1633l1.8814-3.3013a.437.437 0 0
 0-.1633-.5959l-3.3013-1.8814a.437.437 0 0
 0-.5959.1633l-.1444.2534zm4.9282-6.5488a.437.437 0 0 1
 .5972.1584l1.9084 3.2858a.437.437 0 0 1-.1583.5972l-.1035.0601 2.8511
 1.6248.5456-.3169c.5317-.3088.7123-.9901.4035-1.5217l-4.0788-7.0225c-.3088-.5316-.9901-.7123-1.5217-.4035l-7.0224
 4.0788c-.5317.3088-.7123.9901-.4036 1.5217l2.037 3.5071
 1.6291-2.8436-.1277-.22a.437.437 0 0 1
 .1584-.5973m-4.1524.3539h-.2541a.437.437 0 0
 1-.437-.4369V3.9515a.437.437 0 0 1 .437-.4369h3.7997a.437.437 0 0 1
 .437.4369v.1225l2.8369-1.6478V1.791c0-.6148-.4984-1.1132-1.1132-1.1132h-8.121c-.6148
 0-1.1132.4984-1.1132 1.1132v8.121c0 .6148.4984 1.1132 1.1132
 1.1132h4.0561zm-2.4558 3.3328-.1444.2534a.437.437 0 0
 1-.5959.1633l-3.3013-1.8814a.437.437 0 0 1-.1633-.5961L5.5623
 6.159a.437.437 0 0 1
 .5959-.1633l.1554.0886V2.819l-.6279-.3578c-.5342-.3044-1.214-.1182-1.5184.416L.1463
 9.9329c-.3044.5342-.1182 1.214.416 1.5184l7.0557 4.021c.5342.3044
 1.2139.1182 1.5184-.416l2.0123-3.531zm3.2802.9837 2.037
 3.507c.3088.5317.1281 1.213-.4035 1.5218l-7.0225
 4.0787c-.5316.3088-1.213.1282-1.5217-.4035L.1764
 14.1864c-.3088-.5317-.1281-1.213.4035-1.5218l.5457-.3169 2.851
 1.6248-.1035.0601a.437.437 0 0 0-.1584.5973l1.9084 3.2858a.437.437 0
 0 0 .5972.1584l3.2858-1.9084a.437.437 0 0 0 .1584-.5973l-.1278-.22z"
 />
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
