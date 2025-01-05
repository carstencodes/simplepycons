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


class SupabaseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "supabase"

    @property
    def original_file_name(self) -> "str":
        return "supabase.svg"

    @property
    def title(self) -> "str":
        return "Supabase"

    @property
    def primary_color(self) -> "str":
        return "#3FCF8E"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Supabase</title>
     <path d="M11.9 1.036c-.015-.986-1.26-1.41-1.874-.637L.764
 12.05C-.33 13.427.65 15.455 2.409 15.455h9.579l.113 7.51c.014.985
 1.259 1.408
 1.873.636l9.262-11.653c1.093-1.375.113-3.403-1.645-3.403h-9.642z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/supabase/supabase/blob/403
1a7549f5d46da7bc79c01d56be4177dc7c114/packages/common/assets/images/su'''

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
