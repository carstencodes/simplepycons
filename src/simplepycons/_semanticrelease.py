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


class SemanticreleaseIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "semanticrelease"

    @property
    def original_file_name(self) -> "str":
        return "semanticrelease.svg"

    @property
    def title(self) -> "str":
        return "semantic-release"

    @property
    def primary_color(self) -> "str":
        return "#494949"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>semantic-release</title>
     <path d="M11.952 14.4a2.4 2.4 0 1 1 0-4.8 2.4 2.4 0 0 1 0
 4.8zm0-.72a1.68 1.68 0 1 0 0-3.36 1.68 1.68 0 0 0 0 3.36zM8.304
 3.12v1.728c.096.528 1.008 2.64 1.68 3.888C9.12 8.112 7.2 6.672 6.672
 5.952a4.416 4.416 0 0 1-.816-1.392L2.448 6.48v4.128c.432.24 1.104.72
 1.488.864.528.192 2.832.432 4.224.48-1.008.432-3.168 1.392-4.08
 1.488-.768.144-1.296.048-1.632 0v4.08l3.312 1.872c.432-.192
 1.152-.576 1.488-.816.432-.336 1.776-2.208 2.496-3.408-.096
 1.056-.384 3.408-.72 4.272-.288.72-.624 1.104-.816 1.392L12
 22.992l3.504-2.016c.048-.432.096-1.344
 0-1.824-.048-.528-1.008-2.64-1.632-3.888.864.672 2.736 2.112 3.312
 2.832.528.624.72 1.152.816
 1.44l3.552-2.016v-4.032c-.384-.24-1.152-.72-1.632-.912-.48-.192-2.784-.432-4.176-.48
 1.008-.48 3.168-1.392 4.08-1.488.864-.144 1.392-.048
 1.728.048V6.48l-3.36-1.92-1.488.912c-.432.336-1.776 2.208-2.544
 3.36.144-1.056.432-3.408.768-4.272.288-.72.624-1.152.864-1.392L12
 1.008zM12 0l10.416 6v12L12 24 1.584 18V6z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = ''''''
        if len(_value) > 0:
            return _value
        return None

    @property
    def source(self) -> "str":
        return '''https://github.com/semantic-release/semantic-
release/blob/85bc213f04445a9bb8f19e5d45d6ecd7acccf841/media/semantic-r'''

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
