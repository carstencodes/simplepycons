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


class BloglovinIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "bloglovin"

    @property
    def original_file_name(self) -> "str":
        return "bloglovin.svg"

    @property
    def title(self) -> "str":
        return "Bloglovin"

    @property
    def primary_color(self) -> "str":
        return "#000000"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Bloglovin</title>
     <path d="M12.526 11.695c1.84-.382 3.367-2.044 3.367-4.478
 0-2.604-1.9-4.97-5.615-4.97H0v19.506h10.6c3.75 0 5.683-2.341
 5.683-5.292-.009-2.426-1.646-4.444-3.757-4.766zm-8.37-5.793h5.207c1.407
 0 2.28.849 2.28 2.044 0 1.255-.881 2.044-2.28 2.044H4.155zM9.54
 18.098H4.155v-4.444h5.386c1.61 0 2.484.992 2.484 2.222.009 1.399-.932
 2.222-2.484 2.222zM21.396 2.28c-1.255 0-2.315 1.052-2.315 2.307s.882
 2.103 1.993 2.103c.238 0 .467-.025.56-.085-.238 1.052-1.315
 2.282-2.256 2.782l1.611 1.314C22.796 9.422 24 7.462 24
 5.266c0-1.9-1.23-2.985-2.604-2.985Z" />
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
