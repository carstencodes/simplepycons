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


class JetpackComposeIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "jetpackcompose"

    @property
    def original_file_name(self) -> "str":
        return "jetpackcompose.svg"

    @property
    def title(self) -> "str":
        return "Jetpack Compose"

    @property
    def primary_color(self) -> "str":
        return "#4285F4"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Jetpack Compose</title>
     <path d="M12.135.003a2.577 2.577 0 0 0-1.42.344L2.55 5.06a2.577
 2.577 0 0 0-.953.967l3.957 2.17a1.765 1.765 0 0 1
 .603-.588l4.951-2.86a1.761 1.761 0 0 1 1.76 0l4.951 2.86a1.753 1.753
 0 0 1 .526.46l3.921-2.265a2.577 2.577 0 0
 0-.816-.744L13.291.347a2.577 2.577 0 0 0-1.152-.34Zm-.145 4.912a1.36
 1.36 0 0 0-.68.182L6.36 7.953a1.345 1.345 0 0 0-.454.435l1.92
 1.055a1.05 1.05 0 0 1 .31-.275l3.34-1.928a1.054 1.054 0 0 1 1.051
 0l3.336 1.928a1.066 1.066 0 0 1 .238.199l.018-.01-.002-.002
 1.877-1.08a1.353 1.353 0 0 0-.373-.322l-4.95-2.86a1.357 1.357 0 0
 0-.68-.178Zm10.432 1.149-3.92 2.26a1.757 1.757 0 0 1 .2.812v5.715c0
 .627-.332 1.21-.88 1.528l-4.95 2.86a1.761 1.761 0 0
 1-.64.214v4.524a2.577 2.577 0 0 0 1.059-.313l8.162-4.713a2.577 2.577
 0 0 0 1.289-2.23V7.297a2.577 2.577 0 0
 0-.318-1.228Zm-20.937.238a2.577 2.577 0 0 0-.227.99v9.43c0 .918.491
 1.767 1.293 2.229l8.162 4.713a2.57 2.57 0 0 0 1.225.336v-4.531a1.761
 1.761 0 0 1-.833-.235L6.156 16.38a1.765 1.765 0 0
 1-.877-1.528V9.136a1.776 1.776 0 0 1 .131-.676Zm16.67 2.223-1.89
 1.092a1.058 1.058 0 0 1 .124.46v3.856c0 .378-.2.72-.526.907l-3.336
 1.93a1.04 1.04 0 0
 1-.295.107v2.17c.152-.027.304-.078.44-.157l4.949-2.859a1.36 1.36 0 0
 0 .68-1.18V9.136a1.36 1.36 0 0 0-.147-.607Zm-12.387.13a1.36 1.36 0 0
 0-.088.481v5.715a1.36 1.36 0 0 0 .68 1.18l4.95
 2.86c.194.112.412.166.627.177v-2.174a1.054 1.054 0 0 1-.46-.123L8.14
 14.843a1.054 1.054 0 0 1-.532-.908v-3.853a.99.99 0 0 1
 .077-.38l-.034-.013z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://developer.android.com/jetpack/compose'''

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
