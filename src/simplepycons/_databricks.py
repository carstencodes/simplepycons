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


class DatabricksIcon(Icon):
    """"""
    @property
    def name(self) -> "str":
        return "databricks"

    @property
    def original_file_name(self) -> "str":
        return "databricks.svg"

    @property
    def title(self) -> "str":
        return "Databricks"

    @property
    def primary_color(self) -> "str":
        return "#FF3621"

    @property
    def raw_svg(self) -> "str":
        return ''' <svg xmlns="http://www.w3.org/2000/svg"
 role="img" viewBox="0 0 24 24">
    <title>Databricks</title>
     <path d="M.95 14.184L12 20.403l9.919-5.55v2.21L12
 22.662l-10.484-5.96-.565.308v.77L12
 24l11.05-6.218v-4.317l-.515-.309L12 19.118l-9.867-5.653v-2.21L12
 16.805l11.05-6.218V6.32l-.515-.308L12 11.974 2.647 6.681 12
 1.388l7.76 4.368.668-.411v-.566L12 0 .95 6.27v.72L12
 13.207l9.919-5.55v2.26L12 15.52 1.516 9.56l-.565.308Z" />
</svg>'''

    @property
    def guidelines_url(self) -> "str | None":
        _value: "str" = '''https://brand.databricks.com/Styleguide/Guide'''
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
