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


class FirewallaIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "firewalla"

    @property
    def original_file_name(self) -> "str":
        return "firewalla.svg"

    @property
    def title(self) -> "str":
        return "Firewalla"

    @property
    def primary_color(self) -> "str":
        return "#C8332D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Firewalla</title>
     <path d="M12.156 0c-3.602 4.89.391 7.768 2.61 11.893-.751
 1.527-1.745 3.08-2.733
 4.836l-.072.025c-.849-.983-1.99-1.85-3.033-2.967
 2.606-5.783-.809-9.812-.809-9.812a12.555 12.555 0 0 0-1.916
 2.021c-2.296 3.06-2.027 5.897-2.027 5.897C4.176 19.07 12.125 24
 12.125 24a21.738 21.738 0 0 0 2.139-1.594c5.864-4.974 5.564-10.513
 5.564-10.513.122-4.308-1.622-5.905-4.82-9.014A83.864 83.864 0 0 1
 12.156 0zm.281 17.37zm.397.687a4.298 4.298 0 0 1 .14.328 4.463 4.463
 0 0 0-.14-.328zm.266.718a4.289 4.289 0 0 1
 .14.791c.024.286.023.588-.006.91a5.23 5.23 0 0 0 .006-.91 4.513 4.513
 0 0 0-.14-.79z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/firewalla/firewalla/blob/9
7f7463fe07b85b979a8f0738fdf14c1af0249a8/extension/diag/static/firewall'''

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
