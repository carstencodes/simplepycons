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


class WpEngineIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "wpengine"

    @property
    def original_file_name(self) -> "str":
        return "wpengine.svg"

    @property
    def title(self) -> "str":
        return "WP Engine"

    @property
    def primary_color(self) -> "str":
        return "#0ECAD4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>WP Engine</title>
     <path d="M8.145 0v5.867L9.99 7.71h4.022l1.845-1.844V0zm8.145
 0v5.867l1.845 1.844h5.864V.001zM1.845 0L0 1.845v5.866h7.712V0zM0
 8.146v7.71h5.866l1.845-1.844V8.145zm18.133 0L16.29 9.989v4.022l1.845
 1.845H24V8.145zm-6.147 2.75a1.105 1.105 0 00.014 2.21A1.105 1.105 0
 0013.105 12a1.105 1.105 0 00-1.118-1.104zM0
 16.29v7.71h5.866l1.845-1.842v-4.023l-1.845-1.845zm9.988 0l-1.843
 1.845V24h7.71v-5.866L14.01 16.29zm6.3 0V24H24v-5.865l-1.842-1.845z"
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
