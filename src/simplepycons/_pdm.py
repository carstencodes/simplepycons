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


class PdmIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "pdm"

    @property
    def original_file_name(self) -> "str":
        return "pdm.svg"

    @property
    def title(self) -> "str":
        return "PDM"

    @property
    def primary_color(self) -> "str":
        return "#AC75D7"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>PDM</title>
     <path d="M10.44.418a3.12 3.12 0 0 1 3.12 0l7.69 4.44a3.12 3.12 0
 0 1 1.56 2.702v8.88a3.12 3.12 0 0 1-1.56 2.702l-7.69 4.44a3.12 3.12 0
 0 1-3.12 0l-7.69-4.44a3.12 3.12 0 0 1-1.56-2.702V7.56a3.12 3.12 0 0 1
 1.56-2.702Zm3.87 3.315L12.311 2.58a.624.624 0 0 0-.624 0l-7.69
 4.44a.624.624 0 0 0-.312.54v3.774l10.623-6.133Zm2.496 13.643
 1.255.725 1.941-1.12a.624.624 0 0 0 .312-.541V7.56a.624.624 0 0
 0-.312-.54l-3.196-1.845Zm-2.497-1.441V8.083l-6.8 3.926ZM3.686
 14.217v2.223c0 .223.119.429.312.54l7.69 4.44a.624.624 0 0 0 .624
 0l3.252-1.878-10.55-6.091Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/pdm-project/pdm/blob/68aba'''

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
