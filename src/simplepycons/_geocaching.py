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


class GeocachingIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "geocaching"

    @property
    def original_file_name(self) -> "str":
        return "geocaching.svg"

    @property
    def title(self) -> "str":
        return "Geocaching"

    @property
    def primary_color(self) -> "str":
        return "#00874D"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Geocaching</title>
     <path d="M0 11.239h1.918c.151-1.738.841-3.819 2.521-5.498C2.81
 4.532 2.484 3.136 2.484 2.36h.652c.068.682.357 1.656 2.247
 2.753C7.167 4.067 7.532 3.037 7.631 2.36h.652c0 .721-.317 2.082-1.951
 3.38 1.366.89 2.506 2.195 2.928
 4.237H7.576c-.294-1.461-1.04-2.616-2.193-3.504-1.169 1.143-1.774
 3.023-1.811 4.766h6.57V1.098H0v10.141zM5.383 2.63c.469 0
 .85.377.85.842 0 .465-.38.841-.85.841a.846.846 0 0 1-.85-.841.847.847
 0 0 1 .85-.842zM3.574 12.779h6.567v6.567a7.338 7.338 0 0
 1-3.775-1.528L5.195 18.99a8.978 8.978 0 0 0 4.946
 2.012v1.919H0V12.779h1.919a8.98 8.98 0 0 0 2.03
 4.968l1.171-1.171a7.33 7.33 0 0
 1-1.546-3.797zm8.108-11.681h10.142V11.24h-1.919a8.981 8.981 0 0
 0-2.012-4.947l-1.171 1.171a7.338 7.338 0 0 1 1.528
 3.776h-6.568V4.672a7.347 7.347 0 0 1 3.798 1.545l1.171-1.171a8.987
 8.987 0 0 0-4.968-2.03V1.098zm0
 11.681h10.142V22.92h-5.988l-1.172-4.736c.473-.572.965-.836
 2.137-1.018 2.184-.341 2.576-2.232
 2.576-2.232-1.02.245-1.837.001-2.799-.234-.949-.231-1.859-.211-2.727.092-.659.23-.818.445-.818.445l1.907
 7.683h-3.257V12.779zm11.4-11.7a.894.894 0 0 0-.913.918c0
 .521.392.913.913.913A.894.894 0 0 0 24 1.997a.895.895 0 0
 0-.918-.918zm0 1.679a.738.738 0 0
 1-.753-.761c0-.437.319-.764.753-.764.437 0 .759.327.759.764a.741.741
 0 0
 1-.759.761zm.379-.907c0-.201-.149-.298-.327-.298h-.411v.889h.204v-.309h.084l.259.309h.22v-.04l-.251-.28c.118-.028.222-.122.222-.271zm-.335.133h-.199v-.262h.199c.076
 0 .133.044.133.131.001.081-.057.131-.133.131z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://www.geocaching.com/about/logousage.as'''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.geocaching.com/about/logousage.as'''

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
