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


class AboutdotmeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "aboutdotme"

    @property
    def original_file_name(self) -> "str":
        return "aboutdotme.svg"

    @property
    def title(self) -> "str":
        return "About.me"

    @property
    def primary_color(self) -> "str":
        return "#333333"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>About.me</title>
     <path d="M3.158 9.897v4.131h.65v-.408c.23.297.577.483.961.483.768
 0 1.332-.582 1.332-1.573 0-.967-.558-1.568-1.332-1.568-.372
 0-.719.168-.96.49V9.897Zm10.285.322v.818h-.495v.563h.495v1.729c0
 .501.26.774.769.774.297 0 .49-.087.607-.192l-.155-.496a.4.4 0 0
 1-.285.112c-.186
 0-.285-.155-.285-.36V11.6h.607v-.563h-.607v-.818zm-5.488.743c-.954
 0-1.536.706-1.536 1.567 0 .855.582 1.574 1.536 1.574s1.537-.719
 1.537-1.574c0-.86-.583-1.567-1.537-1.567m14.577 0c-.886
 0-1.518.7-1.518 1.567 0 .948.663 1.574 1.567 1.574.47 0 .91-.155
 1.214-.44l-.297-.427c-.217.216-.557.334-.855.334-.564
 0-.898-.378-.948-.824H24v-.16c0-.942-.57-1.624-1.468-1.624m-4.576
 0c-.459
 0-.849.298-.979.477v-.402h-.65v2.991h.65v-2.093c.137-.192.403-.397.694-.397.354
 0 .49.217.49.54v1.95h.65v-2.093c.13-.199.403-.397.694-.397.353 0
 .495.217.495.54v1.95h.65v-2.161c0-.607-.315-.905-.86-.905-.453
 0-.85.28-1.016.545-.1-.322-.372-.545-.818-.545m-16.55 0c-.477
 0-.91.15-1.257.484l.272.452a1.2 1.2 0 0 1 .886-.384c.41 0
 .7.21.7.557v.446c-.223-.254-.563-.384-.972-.384-.49
 0-1.035.285-1.035.979 0 .656.551.99 1.035.99.396 0
 .75-.142.972-.402v.328h.65V12.04c0-.799-.582-1.078-1.25-1.078m8.449.075v2.118c0
 .607.322.948.966.948.47 0 .842-.235
 1.053-.471v.396h.65v-2.991h-.65v2.1a.99.99 0 0 1-.762.39c-.372
 0-.607-.149-.607-.613v-1.877zm12.67.458c.589 0
 .83.434.85.787H21.69c.025-.36.285-.787.837-.787m-17.942.043c.514 0
 .843.415.843.992 0 .582-.329.997-.843.997a.98.98 0 0
 1-.774-.397v-1.189a.98.98 0 0 1 .774-.403m3.372 0c.558 0
 .861.465.861.991 0 .533-.303.998-.86.998-.552 0-.862-.465-.862-.997
 0-.527.31-.992.861-.992m-6.66 1.041c.279 0
 .557.105.712.31v.458c-.155.204-.433.31-.712.31-.366
 0-.644-.21-.644-.539 0-.322.278-.539.644-.539m14.269.65a.44.44 0 0
 0-.434.428c0 .235.198.44.434.44a.445.445 0 0 0 .434-.44.44.44 0 0
 0-.434-.428" />
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
