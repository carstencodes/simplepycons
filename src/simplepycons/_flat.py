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


class FlatIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "flat"

    @property
    def original_file_name(self) -> "str":
        return "flat.svg"

    @property
    def title(self) -> "str":
        return "Flat"

    @property
    def primary_color(self) -> "str":
        return "#3481FE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Flat</title>
     <path d="M6.5455 17.4545v3.2728C6.5455 22.5348 5.0802 24 3.2727
 24S0 22.5348 0 20.7273c0-1.8075 1.4652-3.2728
 3.2727-3.2728Zm8.7272-8.7272V12c0 1.8075-1.4652 3.2727-3.2727
 3.2727H5.4545c-1.8074 0-3.2727-1.4652-3.2727-3.2727 0-1.8075
 1.4653-3.2727 3.2727-3.2727zM24 0v3.2727c0 1.8075-1.4652
 3.2728-3.2727 3.2728H7.6363c-1.8074
 0-3.2727-1.4653-3.2727-3.2728S5.829 0 7.6364 0Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/netless-io/flat/blob/525b2
247f36e96ae2f9e6a39b4fe0967152305f2/desktop/renderer-app/src/assets/im'''

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
