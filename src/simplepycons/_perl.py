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


class PerlIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "perl"

    @property
    def original_file_name(self) -> "str":
        return "perl.svg"

    @property
    def title(self) -> "str":
        return "Perl"

    @property
    def primary_color(self) -> "str":
        return "#0073A1"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Perl</title>
     <path d="M12 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0
 12-12A12 12 0 0 0 12 0m.157 1.103a10.91 10.91 0 0 1 9.214
 5.404c-1.962.152-3.156 1.698-5.132 3.553-2.81
 2.637-4.562.582-5.288-.898-.447-1.004-.847-2.117-1.544-2.769A.4.4 0 0
 1 9.3 6.02l.08-.37a.083.083 0 0
 0-.074-.1c-.33-.022-.601.093-.84.368a2.5 2.5 0 0
 0-.375-.064c-.863-.093-1.036.345-1.873.345H5.81c-.758
 0-1.391.361-1.7.892-.248.424-.257.884.15.93-.126.445.292.62 1.224.192
 0 0 .733.421 1.749.421.549 0 .712.087.914.967.486 2.138 2.404 5.655
 6.282 5.655l.118.166c.659.934.86 2.113.48 3.184-.307.867-.697
 1.531-.697 1.531q.01.178.01.349c0 .81-.175 1.553-.387 2.23a10.91
 10.91 0 0 1-11.989-6.342A10.91 10.91 0 0 1 7.608 2.01a10.9 10.9 0 0 1
 4.55-.907M7.524 6.47c.288 0 .575.231.477.272a.4.4 0 0 1-.1.02.38.38 0
 0 1-.375.327.384.384 0 0 1-.378-.326.4.4 0 0
 1-.101-.02c-.098-.042.19-.273.477-.273m10.193 10.49q.05 0
 .101.007.326.054.694.096.135.01.269.026a13.4 13.4 0 0 0 2.846-.007
 10.9 10.9 0 0 1-2.007
 2.705c-.11-.23-.547-1.19-.573-2.196q-.156-.01-.313-.026-.13-.014-.256-.022a18
 18 0 0 1-.735-.102h-.003c-.032
 0-.06.01-.074.035l-.003.012q-.081.265-.182.544c.428 1.084.652
 2.078.652 2.078.14.22.258.432.363.64a11 11 0 0 1-2.168 1.264 11 11 0
 0 1-1.205.426 13.3 13.3 0 0 1 1.055-2.531s.678-1.445
 1.027-2.564v-.004a.55.55 0 0 1 .512-.38" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/metacpan/perl-assets/blob/'''

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
