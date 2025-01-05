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


class OdnoklassnikiIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "odnoklassniki"

    @property
    def original_file_name(self) -> "str":
        return "odnoklassniki.svg"

    @property
    def title(self) -> "str":
        return "Odnoklassniki"

    @property
    def primary_color(self) -> "str":
        return "#EE8208"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Odnoklassniki</title>
     <path d="M12 0a6.2 6.2 0 0 0-6.194 6.195 6.2 6.2 0 0 0 6.195
 6.192 6.2 6.2 0 0 0 6.193-6.192A6.2 6.2 0 0 0 12.001 0zm0 3.63a2.567
 2.567 0 0 1 2.565 2.565 2.568 2.568 0 0 1-2.564 2.564 2.568 2.568 0 0
 1-2.565-2.564 2.567 2.567 0 0 1 2.565-2.564zM6.807 12.6a1.814 1.814 0
 0 0-.91 3.35 11.611 11.611 0 0 0 3.597 1.49l-3.462 3.463a1.815 1.815
 0 0 0 2.567 2.566L12 20.066l3.405 3.403a1.813 1.813 0 0 0 2.564
 0c.71-.709.71-1.858 0-2.566l-3.462-3.462a11.593 11.593 0 0 0
 3.596-1.49 1.814 1.814 0 1 0-1.932-3.073 7.867 7.867 0 0 1-8.34
 0c-.318-.2-.674-.29-1.024-.278z" />
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
