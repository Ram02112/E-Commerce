$(document).ready(function () {
  $(".add-to-cart-btn").on("click", function () {
    let index = $(this).attr("data-index");

    let quantity = $(".product-quantity-" + index).val();
    let product_title = $(".product-title-" + index).val();
    let product_id = $(".product-id-" + index).val();
    let product_price = $(".product-price-" + index).text();
    let product_pid = $(".product-pid-" + index).val();

    let product_image = $(".product-image-" + index).val();

    console.log(quantity);
    console.log(product_title);
    console.log(product_id);
    console.log(product_price);
    console.log(product_pid);
    console.log(product_image);

    $.ajax({
      url: "/add-to-cart",
      data: {
        id: product_id,
        pid: product_pid,
        image: product_image,
        qty: quantity,
        title: product_title,
        price: product_price,
      },
      dataType: "json",
      beforeSend: function () {
        console.log("====================================");
        console.log("Adding to cart");
        console.log("====================================");
      },
      success: function () {
        console.log("Add to cart successful");
      },
    });
  });

  $(".delete-product").on("click", function () {
    let product_id = $(this).attr("data-item");
    let this_val = $(this);

    console.log(product_id);
    console.log(this_val);

    $.ajax({
      url: "/delete-from-cart",
      data: {
        id: product_id,
      },
      dataType: "json",
      beforeSend: function () {
        this_val.hide();
      },
      success: function (response) {
        this_val.show();
        $("#cart-list").html(response.data);
        location.reload();
      },
    });
  });

  $(".update-product").on("click", function () {
    let product_id = $(this).attr("data-item");
    let this_val = $(this);
    let product_quantity = $(".product-quantity-" + product_id).val();

    console.log(product_id);
    console.log(this_val);
    console.log(product_quantity);
    $.ajax({
      url: "/update-cart",
      data: {
        id: product_id,
        qty: product_quantity,
      },
      dataType: "json",
      beforeSend: function () {
        this_val.hide();
      },
      success: function (response) {
        this_val.show();
        $("#cart-list").html(response.data);
        location.reload();
      },
    });
  });

  $(document).on("click", ".defaultbtn", function () {
    let id = $(this).attr("data-address-id");
    $.ajax({
      url: "/make-default-address",
      data: {
        id: id,
      },
      dataType: "json",
      success: function (response) {
        if (response.boolean == true) {
          $(".check").hide();
          $(".action_btn").show();

          $(".check" + id).show();
          $(".button" + id).hide();
        }
      },
    });
  });

  $(document).on("submit", "#contact-form-ajax", function (e) {
    e.preventDefault();

    let user_name = $("#name").val();
    let email = $("#email").val();
    let phone = $("#phone").val();
    let subject = $("#subject").val();
    let message = $("#message").val();

    $.ajax({
      url: "/ajax-contact-form",
      data: {
        user_name: user_name,
        email: email,
        phone: phone,
        subject: subject,
        message: message,
      },
      dataType: "Json",
      success: function (response) {
        console.log("data sent");
        $("#contact-form-ajax").hide();
        $("#message-response").html("Message sent successfully");
      },
    });
  });
});
