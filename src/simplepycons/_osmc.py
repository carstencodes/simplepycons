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


class OsmcIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "osmc"

    @property
    def original_file_name(self) -> "str":
        return "osmc.svg"

    @property
    def title(self) -> "str":
        return "OSMC"

    @property
    def primary_color(self) -> "str":
        return "#17394A"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>OSMC</title>
     <path d="M22.768 12.002c0 5.935-4.829 10.768-10.768
 10.768-5.935-.005-10.763-4.833-10.763-10.768 0-5.94 4.828-10.767
 10.768-10.767 5.934 0 10.763 4.828 10.763 10.767m.292-4.673a11.913
 11.913 0 0 0-2.57-3.813 11.963 11.963 0 0 0-3.813-2.57A11.857 11.857
 0 0 0 12.005 0a11.926 11.926 0 0 0-8.486 3.516A11.963 11.963 0 0 0
 .948 7.33C.318 8.811.002 10.38.002 12.002s.316 3.192.942 4.673a11.913
 11.913 0 0 0 2.57 3.813A11.963 11.963 0 0 0 12 24c1.619 0 3.191-.32
 4.673-.942a11.913 11.913 0 0 0 3.813-2.57 11.963 11.963 0 0 0
 3.512-8.486c0-1.623-.311-3.191-.938-4.673M8.566 14.631V9.263l2.574
 2.684-2.574 2.684zM7.327 6.296v11.422l8.116-8.455v6.767c0
 .343.279.618.617.618a.622.622 0 0 0 .622-.622v-9.74l-4.677
 4.77-4.678-4.76z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/osmc/website/tree/e7d0d800'''

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
