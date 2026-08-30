#
# SPDX-License-Identifier: MIT
#
# Copyright (c) 2026 Carsten Igel.
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


class TraxsourceIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "traxsource"

    @property
    def original_file_name(self) -> "str":
        return "traxsource.svg"

    @property
    def title(self) -> "str":
        return "Traxsource"

    @property
    def primary_color(self) -> "str":
        return "#40A0FF"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Traxsource</title>
     <path d="M23.068
 10.942c.067-.457.092-.904.101-1.587.073-5.269-4.504-9.32-9.608-9.349a198
 198 0 0 0-3.123 0C5.333.036.77 4.036.83 9.355c.008.669.03 1.14.093
 1.6-.655.957-.992 2.233-.85 3.592l.043.403c.28 2.673 2.305 4.652 4.52
 4.419l.118-.012c1.513 2.836 4.19 4.631 7.244 4.643h.007c.248 0
 .449-.2.449-.45v-1.598a.45.45 0 0 0-.448-.449V21.5c-3.104
 0-5.901-3.795-5.901-7.614 0-3.775 2.797-7.634 5.888-7.634H12c.248 0
 .449-.2.449-.449V4.225a.45.45 0 0 0-.443-.45v-.003C8.675 3.78 5.792
 5.91 4.378 9.2l-.801.084c-.042.005-.081.015-.123.02-.184-3.99
 3.493-6.872 7.434-6.893 1.007-.007 1.511-.007 2.519 0 3.936.021 7.328
 2.91 7.201
 6.904-.061-.01-.122-.024-.185-.03l-1.282-.136v.001l-.012-.002a.507.507
 0 0 0-.558.45l-.953 9.077a.506.506 0 0 0
 .45.557h.013v.002l1.282.134c2.216.233 4.24-1.746
 4.52-4.419l.043-.403c.144-1.366-.197-2.646-.858-3.605" />
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
