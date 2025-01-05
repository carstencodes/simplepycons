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


class UnityIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "unity"

    @property
    def original_file_name(self) -> "str":
        return "unity.svg"

    @property
    def title(self) -> "str":
        return "Unity"

    @property
    def primary_color(self) -> "str":
        return "#FFFFFF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Unity</title>
     <path d="m12.9288 4.2939 3.7997 2.1929c.1366.077.1415.2905 0
 .3675l-4.515 2.6076a.4192.4192 0 0 1-.4246 0L7.274
 6.8543c-.139-.0745-.1415-.293 0-.3675l3.7972-2.193V0L1.3758
 5.5977V16.793l3.7177-2.1456v-4.3858c-.0025-.1565.1813-.2682.318-.1838l4.5148
 2.6076a.4252.4252 0 0 1
 .2136.3676v5.2127c.0025.1565-.1813.2682-.3179.1838l-3.7996-2.1929-3.7178
 2.1457L12 24l9.6954-5.5977-3.7178-2.1457-3.7996
 2.1929c-.1341.082-.3229-.0248-.3179-.1838V13.053c0-.1565.087-.2956.2136-.3676l4.5149-2.6076c.134-.082.3228.0224.3179.1838v4.3858l3.7177
 2.1456V5.5977L12.9288 0Z" />
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
