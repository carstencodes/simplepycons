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


class FreebsdIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "freebsd"

    @property
    def original_file_name(self) -> "str":
        return "freebsd.svg"

    @property
    def title(self) -> "str":
        return "FreeBSD"

    @property
    def primary_color(self) -> "str":
        return "#AB2B28"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>FreeBSD</title>
     <path d="M23.682
 2.406c-.001-.149-.097-.187-.24-.189h-.25v.659h.108v-.282h.102l.17.282h.122l-.184-.29c.102-.012.175-.065.172-.18zm-.382.096v-.193h.13c.06-.002.145.011.143.089.005.09-.08.107-.153.103h-.12zM21.851
 1.49c1.172 1.171-2.077 6.319-2.626
 6.869-.549.548-1.944.044-3.115-1.128-1.172-1.171-1.676-2.566-1.127-3.115.549-.55
 5.697-3.798 6.868-2.626zM1.652 6.61C.626 4.818-.544 2.215.276
 1.395c.81-.81 3.355.319 5.144 1.334A11.003 11.003 0 0 0 1.652
 6.61zm18.95.418a10.584 10.584 0 0 1 1.368 5.218c0 5.874-4.762
 10.636-10.637 10.636C5.459 22.882.697 18.12.697 12.246.697 6.371
 5.459 1.61 11.333 1.61c1.771 0 3.441.433 4.909
 1.199-.361.201-.69.398-.969.574-.428-.077-.778-.017-.998.202-.402.402-.269
 1.245.263 2.2.273.539.701 1.124 1.25 1.674.103.104.208.202.315.297
 1.519 1.446 3.205 2.111 3.829
 1.486.267-.267.297-.728.132-1.287.167-.27.35-.584.538-.927zm2.814-5.088c-.322
 0-.584.266-.584.595s.261.595.584.595c.323 0
 .584-.266.584-.595s-.261-.595-.584-.595zm0 1.087c-.252
 0-.457-.22-.457-.492s.204-.492.457-.492c.252 0
 .457.22.457.492s-.204.492-.457.492z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://www.freebsdfoundation.org/about/proje'''

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
