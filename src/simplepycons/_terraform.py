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


class TerraformIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "terraform"

    @property
    def original_file_name(self) -> "str":
        return "terraform.svg"

    @property
    def title(self) -> "str":
        return "Terraform"

    @property
    def primary_color(self) -> "str":
        return "#844FBA"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Terraform</title>
     <path d="M1.44 0v7.575l6.561 3.79V3.787zm21.12 4.227l-6.561
 3.791v7.574l6.56-3.787zM8.72 4.23v7.575l6.561 3.787V8.018zm0
 8.405v7.575L15.28 24v-7.578z" />
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
