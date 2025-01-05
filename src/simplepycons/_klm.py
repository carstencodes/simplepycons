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


class KlmIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "klm"

    @property
    def original_file_name(self) -> "str":
        return "klm.svg"

    @property
    def title(self) -> "str":
        return "KLM"

    @property
    def primary_color(self) -> "str":
        return "#00A1DE"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>KLM</title>
     <path d="M6.75 13.034H4.5l-2.25
 2.257v-2.257H0v6.018h2.25v-2.257l2.25 2.257h3l-3.375-3.385zm3
 0H7.5v6.018h6v-1.518H9.75zm10.5 0l-1.125 3.385L18
 13.034h-3.75v6.018h2.25v-4.514l1.5
 4.514h2.25l1.5-4.514v4.514H24v-6.018zM10.5 9.649c.725 0 1.313-.589
 1.313-1.316s-.588-1.317-1.313-1.317-1.312.589-1.312 1.317.587 1.316
 1.312 1.316zm1.688-1.316c0 .727.588 1.316 1.312 1.316.725 0
 1.313-.589 1.313-1.316s-.588-1.317-1.313-1.317-1.312.589-1.312
 1.317zm2.999 0c0 .727.588 1.316 1.312 1.316.725 0 1.313-.589
 1.313-1.316s-.588-1.317-1.313-1.317-1.312.589-1.312 1.317zm-6.375
 0c0-.727-.588-1.317-1.313-1.317s-1.312.589-1.312 1.317.588 1.316
 1.313 1.316 1.312-.589 1.312-1.316zM7.5
 10.025h9v1.505h-9zm4.125-2.821h.75v-.752h.75V5.7h-.75v-.753h-.75V5.7h-.75v.752h.75z"
 />
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
