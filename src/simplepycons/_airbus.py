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


class AirbusIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "airbus"

    @property
    def original_file_name(self) -> "str":
        return "airbus.svg"

    @property
    def title(self) -> "str":
        return "Airbus"

    @property
    def primary_color(self) -> "str":
        return "#00205B"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Airbus</title>
     <path d="M11.0673
 11.296c0-.8153-.5311-1.4329-1.6304-1.4329h-2.211v4.2614h1.0375v-3.335H9.437c.4323
 0 .5928.247.5928.5311 0 .2965-.1605.5312-.5928.5312H8.4363l1.4329
 2.2727h1.1858s-.9758-1.5316-.9635-1.5316c.5929-.1359.9758-.5558.9758-1.297M5.4966
 9.8631h1.0376v4.2614H5.4966Zm-3.3227 0L0
 14.137h1.1734l.3459-.7164h1.754l-.4324-.9017h-.877l.6424-1.3093h.0123l1.4575
 2.9274h1.1982L3.1003 9.863Zm12.6854
 2.0504c.3335-.1852.5065-.4693.5065-.9017
 0-.6917-.5188-1.1487-1.3711-1.1487h-2.4333v4.2614h2.5198c.877 0
 1.4575-.4693
 1.4575-1.1981.0123-.494-.2718-.8646-.6794-1.0129m-2.2604-1.1487h1.3835c.21
 0 .3705.1606.3705.3706s-.1606.3705-.3705.3705h-1.3835zm1.4205
 2.4704H12.599v-.8646h1.4205c.247 0 .4447.1852.4447.4323 0
 .247-.1977.4323-.4447.4323m4.8049-.9882c0 .6423-.2964 1.0005-.8893
 1.0005-.5806 0-.877-.3582-.877-1.0005V9.8631h-1.0623v2.3098c0
 1.3217.6917 2.0504 1.9516 2.0504 1.26 0 1.9516-.7287
 1.9516-2.0504V9.8631h-1.0623v2.384zm3.8414-.6793c-.9881-.2347-1.1981-.2594-1.1981-.5435
 0-.2223.247-.3211.667-.3211.5558 0 1.1364.1358
 1.4699.3458l.3335-.8646c-.4447-.247-1.0623-.4076-1.8034-.4076-1.0993
 0-1.717.5434-1.717 1.2846 0 .7905.4571 1.1116 1.5194 1.334.8276.1852
 1.0005.2964 1.0005.531 0 .2471-.2224.3583-.6794.3583-.6546
 0-1.2352-.1606-1.7045-.42l-.3212.914c.5188.2718 1.2846.4447
 2.0504.4447 1.0746 0 1.717-.494
 1.717-1.334.0123-.6793-.42-1.1116-1.334-1.3216" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://brand.airbus.com/en/asset-library/air'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://brand.airbus.com/en/asset-library/air'''

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
